# AI Group Project

# Rap Project

- ## Input/Output Behavior

- ## Project Scope

- ## Metric for Success

- ## Concrete Examples of Inputs and Outputs

- ## Baseline and Oracle

- ## Challenges, techniques to address them

- ## Similar Projects



# Facebook Spam/Negative Comments Detection

- ## Input/Output Behavior
    - Given a facebook post, output whether it is off topic or derogatory

- ## Project Scope
    - The scope of the problem doesn't seem very large. Each input would be a single facebook
    post or comment, and we can acquire a great deal of data by scraping the Facebook groups we are all
    a part of using the Facebook API. We would manually have to categorize the data we collect as either
    on/off topic or derogatory/non-derogatory, but we could write some basic scripts to make this process
    as painless as possible. 
    - It seems reasonable to say that we can build a system that determines whether or not a post is on topic, especially
    with the great deal of data that is available.
    - We could potentially expand the scope past just facebook. Given enough data, we could determine whether a post
    is appropriate on any internet forum. That might expand the scope, but it doesn't seem like it would by much.

- ## Metric for Success
    - How many posts are correctly classified?
        - Here is where an issue arises: In the project spec, they state that applying binary classification is probably not enough.
            - They claim its too narrow...
        - So what would be a better metric for success?
            - Maybe we could expand it a bit so that given a set of posts in a group, our system determines to what degree the community
            of the group is welcoming?
                - That could be interesting!
                - But that seems to be a very qualitative metric. How would we measure that?

- ## Concrete Examples of Inputs and Outputs
    - I can write up a web scraper to get this by the end of the week

- ## Baseline and Oracle
    - An easy baseline would just be binary classification using word features.
    - But what would we use as an Oracle...?
        - Ripped straight from the example in the project proposal: determine if a post is on topic based on the number of comments?

- ## Challenges, techniques to address them

- ## Similar Projects
    - Where I got the idea, some dudes built a similar system as a hackathon: [Facebook mark and sweep](https://github.com/jxnl/fbmarkandsweep/tree/master/old_version/src/utils)
