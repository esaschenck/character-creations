
//quiz from https://www.javatpoint.com/how-to-get-all-checked-checkbox-value-in-javascript and https://www.w3schools.com/html/html_form_input_types.asp


// hide/show elements from https://stackoverflow.com/questions/6242976/javascript-hide-show-element
document.getElementById("pg2").style.visibility = "hidden";


function getCheckboxValue(option) {
  var hairColor = document.getElementById("hairColor");
  var age = document.getElementById("age");
  var skinTone = document.getElementById("skinTone");
  var gender = document.getElementById("gender");
  var weight = document.getElementById("weight");
  var hairTexture = document.getElementById("hairTexture");
  var makeup = document.getElementById("makeup");
  var glasses = document.getElementById("glasses");
  var mustache = document.getElementById("mustache");


  var numChecked = 0;
  res = '';

  if (hairColor.checked == true){
    var value = (document.getElementById("hairColor").value) + ",";
    res = value
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
    }
  

  if (age.checked == true){
    var value = (document.getElementById("age").value) + ",";
    res = res + value;
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (skinTone.checked == true){
    value = (document.getElementById("skinTone").value) + ",";
    res = res + value;
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (gender.checked == true){
    value = (document.getElementById("gender").value) + ",";
    res = res + value;
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (weight.checked == true){
    value = (document.getElementById("weight").value) + ",";
    res = res + value
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (hairTexture.checked == true){
    value = (document.getElementById("hairTexture").value) + ",";
    res = res + value; 
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (makeup.checked == true){
    value = (document.getElementById("makeup").value) + ",";
    res = res + value
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (glasses.checked == true){
    value = (document.getElementById("glasses").value) + ",";
    res = res + value
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 

  if (mustache.checked == true){
    value = (document.getElementById("mustache").value) + ",";
    res = res + value;
    numChecked += 1;
    optionNum = "option" + numChecked;
    localStorage.setItem(optionNum, value);
  } 


  if (option == 1) {
    if (numChecked !== 3) {
      statement = 'Please select three variables';
    }  else if (numChecked == 3) {
      statement = 'Great! Please go to the next page';
  }
  return document.getElementById("result").innerHTML = statement;
  }
  
  if (option == 2) {
    return localStorage.setItem("res", res);
  }
  

}


function makeVisible(id) {
  document.getElementById(id).style.visibility = "visible";
}


function doThings() {
  getCheckboxValue(1);
  getCheckboxValue(2);
  makeVisible("pg2");
}


// SECOND PAGE

//retrieve localstorage res


function retrieveStorage() {
  options = localStorage.getItem("option1") + localStorage.getItem("option2") + localStorage.getItem("option3")
  return document.getElementById("localstorage").innerHTML = options;
}


//this shows the questions
function revealQ1() {
  return document.getElementById("question1").innerHTML = localStorage.getItem("option1");
}
function revealQ2() {
  return document.getElementById("choice2").innerHTML = localStorage.getItem("option2");
}
function revealQ3() {
  return document.getElementById("choice2").innerHTML = localStorage.getItem("option3");
}
  



function submitChoices() {

  return document.getElementById("answer").innerHTML = res;
}






// the options for variables we have are: (note that this isn't a complete list of the available variables, it's just the ones that I want to offer to users)
/*
Black_Hair 
Blond_Hair 
Brown_Hair 
Chubby 
Eyeglasses  
Gray_Hair 
Heavy_Makeup 
Male 
Pale_Skin 
Straight_Hair 
Wavy_Hair 
Young 
*/