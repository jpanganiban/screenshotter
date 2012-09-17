var page = new WebPage();
var url = phantom.args[0];
var filename = phantom.args[1];

console.log(url);
console.log(filename);


page.viewportSize = {width: 1024, height: 768};
page.open(url, function(status) {

    page.render(filename);
    phantom.exit();

});
