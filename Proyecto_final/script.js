var cheerio = require('cheerio');
var jsonframe = require('jsonframe-cheerio');
var $ = require('jquery')

$(function() {
    $('#btnIngresar').click(function() {
        var c = document.getElementById('dns').value;
        console.log(c);
        let $ = cheerio.load(`
        <body>
            <h1>I love jsonframe!</h1>
            <span itemprop="email"> Email: gabin@datascraper.pro  </span>
        <body>`)
        jsonframe($); // initializes the plugin
        let frame = {
            "title": "h1", // this is an inline selector
            "email": "span[itemprop=email] < email" // output an extracted email
        }
        console.log($('body').scrape(frame, { string: true }))
    });
});



var scraping = function () {
    // let cheerio = require('cheerio');
    // let jsonframe = require('jsonframe-cheerio');
}


/*=> output
{
	"title": "I love jsonframe!",
	"email": "gabin@datascraper.pro"
}
*/
