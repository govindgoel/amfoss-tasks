require 'nokogiri'
require 'open-uri'

doc = Nokogiri::HTML(open('https://google.com/search?q=linux&num=20'))

count = 0
doc.search('a div').each do |link|
  if link.content.include? "http"
    puts link.content
    count+=1
  end
  if count == 10
    break
  end
end
