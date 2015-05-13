Title: Beer Festivals + Indirection
Date: 2015-05-13 05:08
Category: Articles
Tags: festival, indirection, decoupling, hi fi
Summary: You can't go straight there.

Now that Mother's Day has passed, it's safe to talk about Father's Day. And Father's Day in the northwest means the [Washington Brewer's Festival](http://washingtonbeer.com/festivals/washington-brewers-festival.php). It's a huge outdoor beer festival with over 400 beers from 105 breweries. Basically heaven for a beer fan like me. Each year, I try to use my tasting tokens only on beers I've never tried before. Ideally, only from breweries I've never tried before. That's usually possible since we have so many here.

Wait, 400 beers and 105 breweries? How the heck do I find what I want to try? Thinking back to last time, this seems like a great place for an [index]({filename}/2015-bjcp-guidelines.md). And no surprise, the folks who run this festival provide an index. At the door you receive a list of breweries in alphabetical order, the beers they expect to be pouring, and their location on a map of the park. So my process for acquiring a taste of a new beer goes something like this:

1. Scan the list of breweries for an unfamiliar name
2. Determine a beer that sounds promising
3. Use their map coordinates to locate their position on the map
4. Use the map to figure out how to walk from where I am to where the brewer is

Did you notice there are actually two index lookups in the above process? The first one was when I went from brewer name to map coordinate &mdash; something like "[Hi Fi Brewing](http://www.hifibrewing.com) will be in the orange tent at B-5". The second one was when I used coordinates B-5 to find out where the orange tent is on the map. Yes, those coordinates are acting as a two-dimensional index into the map!

That's really powerful. With just two index lookups, I was able to go from a brewery's name to an exact location on a map. We see this pattern often in computer science, so much so that it has a name: [Indirection](http://en.wikipedia.org/wiki/Indirection). Indirection is the idea that instead of doing something directly ("walk around the park looking for a brewery you've never heard of"), we do it indirectly ("first read a list of breweries, look up their location on the map, then check the map to see where they are"). If not for the double lookup in the map, I could wander the park all day. With indirection, there's a bit more up-front cost, but the pay-off is much quicker access to the end result.

The other great thing about indirection is its ability to decouple unrelated portions of a task. For instance, today there's a paper map of the park that I have to carry around with me. The good folks at the [Washington Beer Commission](http://washingtonbeer.com/) could decide instead to shoot giant beams of light up from the various tents, tinted to coordinate with the tent color. Then instead of using a map, I could just look into the sky for the beam representing the tent color I want to visit. Nothing else about my workflow would have to change other than swapping the map lookup for an actual lookup. Get it? Look *up*... in the sky... nevermind.

Or they could just make an app with the brewery names. That might be easier than overpowering the [midday June sun in Seattle](https://www.flickr.com/photos/emma_daly/4425625426/).