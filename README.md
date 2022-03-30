# Apprise Property
## Ever struggled with estate agent websites? We're here to help with our accurate property valuations and helpful alerts to notify you when a new property is listed. Perfect for both sellers and buyers.

## Inspiration
As students, we struggled with the rapid turnover of property listings on Durham estate agents websites. We aimed to make a solution that:
- Unites buyers and sellers,
- Is ergonomic and accessible,
- Gives customers peace of mind that they will never miss out on their dream home,

## What it does
Our website is for both people looking to buy properties and people selling properties. Buyers can sign up for notifications for all of the properties on the market. Sellers can get simple, accurate property valuations at the click of a button. Through this unified website, we can unite buyers and sellers to streamline the process of property transactions.

## How we built it
- Used web scraping code to periodically collect data about properties currently on the market.
- Use said data to compare the sellers' properties with similar ones to get a valuation.
- Use the same data to find new properties to send to the buyers.
- Used twilio to send out SMS notifications to customers.

## Challenges we ran into
- Issues with passing data between each specialised python script.
- Sorting the mass amounts of data we received from the web-scraping.

## Accomplishments that we're proud of
-Our collaboration and teamwork on this project,
-Having an end product that can solve real life issues.

## What we learned
- We've learnt about new programming features such as twilio and web-scraping. We've also learnt about how much you need to persevere on coding projects.

## What's next for Apprise Property
-Next we're looking to enable the sellers to upload their property to our site so that our buyers get immediately notified; thus cutting out the need for the 'middle men'.
-We'd also be able to easily expand by using multiple data sets from different estate agents to compile all listings into one space and improve the ease of house hunting. Having a larger sample size would also improve the accuracy of our property valuation feature.
-We'd like to be able to add more filters to our listing notification system so that our customers get suggested the best homes for them.
- The R^2 score for our model is currently 0.41. In order to improve this further, we want to increase the number of features included in the model by scraping more data

## Built With
- css
- database
- flask
- html
- javascript
- python
- twilio
