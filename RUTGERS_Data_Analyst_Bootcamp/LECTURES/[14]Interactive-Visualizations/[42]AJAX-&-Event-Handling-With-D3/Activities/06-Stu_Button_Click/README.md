# Vote Star Wars

In this activity, you will use D3 to create click handlers for upvotes and downvotes.

## Instructions

* Use the starter files `index.html`, `static/js/app.js`, and `static/css/style.css` provided in the [Unsolved](Unsolved) folder.

* Use D3 to select the `upvote` and `downvote` buttons on the page.

* Create click handlers for the upvote and downvote buttons.

* The click handlers should do the following:

  * Select the current vote count from the `<h3>` tag.
  * Increment or decrement the count depending on which button was selected.
  * Update the vote count `<h3>` tag using D3.

## Bonus

* Use an array to save information about each vote:

  * Store whether it was an upvote or downvote.
  * Store the current count at each click.
  * Use an array of arrays or an array of objects to store the data.

## Hint

* Don't forget to use the `.on` function to attach the click handlers to the buttons.

* You will need one click handler for each button.

* In Python, you can convert a number in string format into a numeric format using `int()`. In JavaScript, you perform the same operation with the `parseInt()` method. You will need to use `parseInt()` to convert the `<h3>` vote count to a number before you can add or subtract from it.

* Review the [JavaScript parseInt() documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
