# About Project

This is an scrapy spider project to fetch all inspirational quotes from [brainyquote.com ](http://www.brainyquote.com/quotes/topics/topic_inspirational.html) website.

# Running project file

To run this quotes spider project. first open your terminal and  go to spider directory in inspirantion quptes project file , then run the below command to check the scrapy data from brainyquote website.

``` python
scrapy crawl quotes
```

To save the output data to an csv file you can run the below command in your terminal

``` python
scrapy crawl quotes -t csv -o output_filename.csv

```