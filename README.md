<div align="center">

# IT Job TopCV Crawler

</div>
# Overview
- This repo crawls data about IT jobs from [TopCV.vn (IT Jobs category)](https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&company_field=0&sort=up_top&page)
- Data can be crawled from a specific webpage or consecutive webpages
# Requirements:
- requests
- beautifulsoup4
# How to run
## Custom run
- In bash shell, type `python3 crawler.py a b`, where `a`, `b` are the index of webpage
- This command will crawl data from consecutive webpages from page `a` to page `b`
## Default Run
- Use `run.sh` to start crawling
- This bash scipt will execute simultaneously 14 thread
- Each thread crawl data from 10 consecutive pages (1-9,10-19,20-29,...) and save to file naming `recruit_a_b.json` (so there are 14 files after all)
# Result
Data is stored in this [repo](https://github.com/tienlonghungson/BigData-HDFS-Spark-Elasticsearch-Kibana)
# Author:
- [tienlonghungson](https://github.com/tienlonghungson)
- [Sang Cac](https://github.com/sang-20183873)