var cheerio = require('cheerio');
var request = require('request');
var q = require('jquery');

q(function () {
    q('#btnIngresar').click(function () {
        var c = document.getElementById('dns').value;
        console.log(c);
        request(c, 
            (error, res, body) => {
            if (error) return console.log(error);
            if (res.statusCode == 200) return scraping(body);
            return console.log("ERROR INTERNO");
            });
        });
});
function scraping(body){
    let $ = cheerio.load(body);
    $('div.section', 'div.body').each((index, el)=>{
        console.log($('h1', el).text());
        console.log($('p', el).text());
    });
}