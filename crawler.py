import argparse
import json
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def setup_file(filename,is_append):
    if is_append:
        mod = "a+"
        bra = ']'
    else :
        mod = "w"
        bra = '['
    with open(filename, mod) as f:
        f.writelines(bra)

def write_file(filename, data, deli):
    with open(filename,"a+") as f:
        f.writelines(deli)
        json.dump(data,f,indent=2,ensure_ascii=False)

def add_contents(contents,data):
    for header in contents.find_all('h2'):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                # print (nextNode.strip())
                pass
            if isinstance(nextNode, Tag):
                if nextNode.name == "h2":
                    break
                # print (nextNode.get_text(strip=True).strip())
                data[header.text]=nextNode.get_text(strip=True).strip()

def get_list_link(start, end):  
    links = []
    for i in range(start,end+1):
        links.append("https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&company_field=0&sort=up_top&page=" + str(i))
    return links

def get_titles(list_link):
    titles = []
    for link in list_link :
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.findAll('h3', class_='title')
        for tit in title:
            titles.append(tit)
    return titles
# links_company = [link_company.find('a').attrs["href"] for link_company in titles]

def get_links_company(titles): 
    links_company =[]
    for link_company in titles:
        link_obj = link_company.find('a',class_="underline-box-job",href=True)
        if link_obj!= None:
            link = link_obj['href']
            links_company.append(link)
    return links_company
    

def crawl_contents(filename,links_company):
    setup_file(filename,False)
    deli = ""

    for link in links_company:
        news = requests.get(link)
        soup = BeautifulSoup(news.content, "html.parser")
        names_obj = soup.find('a', class_="company-logo")
        if names_obj == None :
            continue
        names = names_obj.attrs["title"]    
        contents= soup.find("div", class_="job-data")
    
  
        data= {} 
        data['name']=names
        add_contents(contents,data)

        write_file(filename, data, deli)
        deli = ",\n"
        print(data)
    setup_file(filename,True)

if __name__=="__main__":
    # create parser
    print("Parsing Args")
    parser = argparse.ArgumentParser()
    parser.add_argument("start")
    parser.add_argument("end")
    args = parser.parse_args()
 
    print("Start crawling from ",args.start," to ",args.end)
    # data = read_data(args.data_file_name)
    links = get_list_link(int(args.start),int(args.end))
    print("list of links")
    print(links)
    title = get_titles(links)
    links_company = get_links_company(title)
    filename = "recruit_"+args.start+"_"+args.end+".json"
    crawl_contents(filename, links_company)