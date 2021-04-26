// dynamically increase height of post-input
var input = document.querySelector('#task__description');
input.addEventListener('input', resizeInput);
resizeInput.call(input);


function resizeInput() {
  var numberOfNL = (this.value.match(/\n/g)||[]).length
  this.style.height = 5 + this.value.length * 0.015 + numberOfNL*1.5 + "em" ;
}
// end //


// hides and shows input field on-click
var hider_button = document.getElementById("hider")
var input_fields = document.querySelectorAll('.can__hide__input');
var hidden = false
var decider;
var resize;
var text;
var w;
var m;

document.getElementById("hider").addEventListener('click', hideFields);
function hideFields() {
  if (hidden === false) {
    decider = 'none'
    resize = 100
    text = 'Unhide'
    hidden = true
    w = 0
    m = 5
  } else {
    decider = 'block'
    resize = 15
    text = 'Hide'
    hidden = false
    w = 100
    m = 0
  }


  document.getElementById("submit").style.width = w + '%'

  setTimeout(myFunction, 450);
  function myFunction() {
  input_fields.forEach(function(i) {
    i.style.display = decider
      }
  )
  }
  hider_button.style.width = resize + '%'
  hider_button.value = text
  hider_button.style.marginBottom = m + '%'
}
