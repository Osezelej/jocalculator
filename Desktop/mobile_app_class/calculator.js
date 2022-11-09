// // dom tree
// console.log(document.firstElementChild.lastElementChild.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.firstElementChild.firstElementChild)

// // id
// console.log(document.getElementById('clear'))

// // className

// console.log(document.getElementsByClassName('btn-operator').length)

// // tag name

// console.log(document.getElementsByTagName('button').length)

// query selector
let numberButtons = document.querySelectorAll('.btn-number');
var displayText = '';
var calText = ''
let isBraOpen;
let isBraClose;
let isequalsPressed;
for (let i=0; i < numberButtons.length; i++){
    numberButtons[i].addEventListener('click', handleClick)
}

let operatorButtons = document.querySelectorAll('.btn-operator');
for (let i=0; i < operatorButtons.length; i++){
    operatorButtons[i].addEventListener('click', handleClick)
}

function handleClick(event){
    if (event.target.innerText == '÷'){
        calText += '/'
    }else if (event.target.innerText == '×'){
        calText += '*'
    }else if(event.target.innerText == '('){
        if (calText[displayText.length - 1] == '*'){

            calText += '('
            isBraOpen = true
        }else{
            calText += '*('
            isBraOpen = true
        }
    }else if(event.target.innerText == ')'){
        calText += ')'
        isBraClose = true
    }
    else{
        calText += event.target.innerText
    }

    displayText += event.target.innerText;
    
   document.getElementById('question').innerText =  displayText;
}

document.getElementById('clear').addEventListener('click', ()=>{
    displayText =''
    calText = ''
    document.getElementById('question').innerText =  displayText;
    document.getElementById('answer').innerText =  displayText;
})


document.getElementById('equal').addEventListener('click', ()=>{
    if (isBraOpen){
        if(isBraClose){
           let data = calText.slice(calText.indexOf('(') + 1, calText.indexOf(')'))
           let answer = eval(data)
           calText = calText.slice(0, calText.indexOf('(')) + answer
           document.getElementById('answer').innerText =  eval(calText)
        }else{
            alert('MATH ERROR PLEASE CLOSE BRACKET')
        }
    }else{
        document.getElementById('answer').innerText =  eval(calText)
    }
    isequalsPressed += 1;
})

document.getElementById('backspace').addEventListener('click', ()=>{
    if (isequalsPressed){
        if (displayText[displayText.length - 1] == '(' || (displayText[displayText.length - 1] == ')')){
 
        }else{
         calText = calText.slice(0, calText.length - 1);
        }
        if(displayText[displayText.length - 1] == '('){
            calText = calText.slice(0, calText.length - 1);
        }
       
    }else{
        displayText = displayText.slice(0, displayText.length - 1);
        calText = calText.slice(0, calText.length - 1);
    }
   
   
    document.getElementById('question').innerText =  displayText;
    if (displayText.indexOf('(') >= 0){
        isBraOpen = true
    }else{
        isBraOpen = false
    }
    if(displayText.indexOf(')') >= 0){
        isBraClose = true
    }else{
        isBraClose = false
    }
})

