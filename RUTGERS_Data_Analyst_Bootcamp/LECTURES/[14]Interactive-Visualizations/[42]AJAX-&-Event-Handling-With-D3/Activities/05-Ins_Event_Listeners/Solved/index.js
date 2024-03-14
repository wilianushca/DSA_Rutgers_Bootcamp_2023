// Getting a reference to the button on the page with the id property set to `click-me`
let button = d3.select("#click-me");

// Getting a reference to the input element on the page with the id property set to 'input-field'
let inputField = d3.select("#input-field");

// This function is triggered when the button is clicked
function handleClick(event) {
  console.log("A button was clicked!");

  // We can use d3 to see the object that dispatched the event
  console.log(event.target);
}

// We can use the `on` function in d3 to attach an event to the handler function
button.on("click", handleClick);

// You can also define the click handler inline
button.on("click", function(event) {
  console.log("Hi, a button was clicked!");
  console.log(event.target);
});

// Event handlers are just normal functions that can do anything you want
button.on("click", function() {
  // Image reference source: https://en.wikipedia.org/wiki/Space_telescope#/media/File:HST-SM4.jpeg
  // The Hubble Space Telescope as seen from the departing Space Shuttle Atlantis, flying STS-125, HST Servicing Mission 4.
  // Wikipedia/Public Domain
  d3.select(".wiki-me").html("<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/HST-SM4.jpeg/440px-HST-SM4.jpeg' alt='space telescope'>");
});

// Input fields can trigger a change event when new text is entered.
inputField.on("change", function(event) {
  let newText = event.target.value;
  console.log(newText);
});
