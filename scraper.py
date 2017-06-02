import scraperwiki
import urllib2
import lxml.etree
import lxml.html


pdfdata = urllib2.urlopen("https://www.ok.gov/osbi/documents/Crime%20in%20Oklahoma%202016%20Final%205.26.17.pdf").read()
#...Then using pdftoxml to convert that into a variable called 'xmldata'
xmldata = scraperwiki.pdftoxml(pdfdata)
#...Then using .fromstring to convert that into a variable called 'pdfxml'
pdfxml = lxml.etree.fromstring(xmldata)
print xmldata
    
#def scrape_and_look_for_next_link(url):
    #scrapes the page and puts it in 'html'
   # html = scraperwiki.scrape(url)
    #print html
    #turns html from a string into an lxml object called 'root'
    #root = lxml.html.fromstring(html)
    #runs another function - created earlier - on 'root'
    #scrapetable(root)

#This will be used for relative links in later pages
#baseurl = "https://www.ok.gov"
#When added to the baseurl, this is our starting page 
#startingurl = "/osbi/documents/Crime%20in%20Oklahoma%202016%20Final%205.26.17.pdf

#Run the function created earlier above on that URL
#scrape_and_look_for_next_link(baseurl+startingurl)
