function scraping() {
    var c = document.getElementById('dns').value;
    console.log(c);
    let cheerio = require('cheerio');
    let $ = cheerio.load(`
	<body>
		<h1>I love jsonframe!</h1>
		<span itemprop="email"> Email: gabin@datascraper.pro  </span>
	<body>`)
    let jsonframe = require('jsonframe-cheerio');
    jsonframe($); // initializes the plugin
    let frame = {
        "title": "h1", // this is an inline selector
        "email": "span[itemprop=email] < email" // output an extracted email
    }
    console.log($('body').scrape(frame, { string: true }))
}
/*=> output
{
	"title": "I love jsonframe!",
	"email": "gabin@datascraper.pro"
}
*/
