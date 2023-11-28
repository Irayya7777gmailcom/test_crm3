var clickableDiv = document.getElementById('clickableDiv');
var hiddenDiv = document.getElementById('hiddenDiv');
var subdiv=document.getElementById('subhiddendiv')
clickableDiv.addEventListener('click', function () {
    if (hiddenDiv.style.display = 'none') {
        hiddenDiv.style.display = 'block';
    } 
});

var closeBtn=document.getElementById('close-btn')
closeBtn.addEventListener('click',()=>{
    hiddenDiv.style.display = 'none'
})

// ADD FIELDS TO DIV
var buttons = document.querySelectorAll(".custom-btn");

buttons.forEach(button => {
    button.addEventListener("click", clicking);
});

function clicking(event){
    var clickedButton = event.target;
    var selectedbuttonfield=clickedButton.getAttribute('data-searchfield')
    var btn = document.createElement('button');
    btn.textContent = selectedbuttonfield;
    btn.setAttribute('data-searchfield', selectedbuttonfield);
    btn.setAttribute('class','clickable-div-btn');
	clickableDiv.appendChild(btn);
    // console.log(btn.getAttribute('class'))
}



// TIME-DIV
function addFromToData(b){
    var btn = document.createElement('button');
    btn.textContent = b;
    btn.setAttribute('data-searchfield', b);
    btn.setAttribute('class','clickable-div-btn');
	clickableDiv.appendChild(btn);
}

function addFromDate(){
    var timeButton=document.getElementById('from-date-btn')
    var fromDate=document.getElementById('from-date').value
    addFromToData(fromDate)
}

function addToDate(){
    var timeButton=document.getElementById('to-date-btn')
    var toDate=document.getElementById('to-date').value
    addFromToData(toDate)
}

// URL
function send() {
const buttons = document.querySelectorAll("#clickableDiv .clickable-div-btn");
var selectedData=[]
buttons.forEach(button => {
    const searchfieldValue = button.getAttribute("data-searchfield");
   selectedData.push(searchfieldValue)
//    console.log(searchfieldValue)
});
// var url="/search/" + user_Id + "/" + model_name + "/" + selectedData.join('/')
var url=selectedData.join('/')
console.log("{% url 'assigned_lead'"+"%}")
}

// CLEAR THE FIELD
// const clearButton = document.getElementById('clearButton');
// clearButton.addEventListener('click', clearButtons);

// function clearButtons() {
//     const buttons = clickableDiv.getElementsByClassName('clickable-div-btn');
//     if (buttons.length > 0) {
//        clickableDiv.removeChild(clickableDiv.lastChild);
//     }
// }


// CLEAR THE FIELD
const showButton = document.getElementById("search-clear");

function hasButtons() {
  const buttons = clickableDiv.querySelectorAll("button");
  return buttons.length > 0;
}

function toggleShowButton() {
  if (hasButtons()) {
    showButton.style.color = "black";
  } else {
    showButton.style.color = "white";
  }
}

toggleShowButton();

//event listener for the div to check for changes in its content
clickableDiv.addEventListener("DOMSubtreeModified", toggleShowButton);

function clearButtons() {
    const buttons = clickableDiv.getElementsByClassName('clickable-div-btn');
    if (buttons.length > 0) {
       clickableDiv.removeChild(clickableDiv.lastChild);
    }
}

