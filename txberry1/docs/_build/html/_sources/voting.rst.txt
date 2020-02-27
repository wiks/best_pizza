Voting
======

Voting do not use any authorization and cookies, becouse this was allowed in task description,
and this allow us to observe how AngularJS dynamically and live changes results.
Of course in real we should use one of noticed method to dissalow multiple voting.

When user click pizza (name or image), Javascript call POST method with pissa ID, and backend
django function **vote** add one to count voting chosen pizza, and add one for all its toppings.
As result we can see sum of pizza votes and five most populat toppings.


