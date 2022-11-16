const themeArr = [
    {
        backgroundColor: 'white',
        buttonBackgroundColor: 'black',
        calBackGroungColor: 'rgb(105, 214, 214)',
        textColor: 'white',
    },
    {
        backgroundColor: '#FD841F',
        buttonBackgroundColor: '#001253',
        backgroundImage: `url("data:image/svg+xml,<svg id='patternId' width='100%' height='100%' xmlns='http://www.w3.org/2000/svg'><defs><pattern id='a' patternUnits='userSpaceOnUse' width='20' height='20' patternTransform='scale(6) rotate(50)'><rect x='0' y='0' width='100%' height='100%' fill='hsla(0,0%,100%,1)'/><path d='M10-10L20 0v10L10 0zM20 0L10-10V0l10 10zm0 10L10 0v10l10 10zm0 10L10 10v10l10 10zM0 20l10-10v10L0 30zm0-10L10 0v10L0 20zM0 0l10-10V0L0 10z'  stroke-width='0.5' stroke='hsla(259, 21%, 86%, 0.27)' fill='none'/></pattern></defs><rect width='800%' height='800%' transform='translate(-144,-78)' fill='url(%23a)'/></svg>")`,
        calBackGroungColor: '#3E6D9C',
        textColor: 'white',

    },
    {
        backgroundColor: '#E3C770',
        buttonBackgroundColor: '#F3E0B5',
        backgroundImage: `url("data:image/svg+xml,<svg id='patternId' width='100%' height='100%' xmlns='http://www.w3.org/2000/svg'><defs><pattern id='a' patternUnits='userSpaceOnUse' width='20' height='20' patternTransform='scale(4) rotate(0)'><rect x='0' y='0' width='100%' height='100%' fill='hsla(0,0%,100%,1)'/><path d='M10-6V6M10 14v12M26 10H14M6 10H-6'  stroke-linecap='square' stroke-width='0.5' stroke='hsla(259, 14%, 88%, 0.4)' fill='none'/></pattern></defs><rect width='800%' height='800%' transform='translate(0,0)' fill='url(%23a)'/></svg>")`,
        calBackGroungColor: '#FFAE6D',
        textColor: 'white',
    },
    {
        backgroundColor: '#5F9DF7',
        buttonBackgroundColor: '#1746A2',
        backgroundImage: `url("data:image/svg+xml,<svg id='patternId' width='100%' height='100%' xmlns='http://www.w3.org/2000/svg'><defs><pattern id='a' patternUnits='userSpaceOnUse' width='30' height='30' patternTransform='scale(2) rotate(0)'><rect x='0' y='0' width='100%' height='100%' fill='hsla(0,0%,100%,1)'/><path d='M0 22.5h30v15H0zm15-15h30v15H15m-30-15h30v15h-30zm15-15h30v15H0z'  stroke-width='1' stroke='hsla(258.5,59.4%,59.4%,1)' fill='none'/></pattern></defs><rect width='800%' height='800%' transform='translate(0,0)' fill='url(%23a)'/></svg>")`,
        calBackGroungColor: '#FF731D',
        textColor: 'white',
    },
    {
        backgroundColor: '#B1D7B4',
        buttonBackgroundColor: '#FFC090',
        backgroundImage: `url("data:image/svg+xml,<svg id='patternId' width='100%' height='100%' xmlns='http://www.w3.org/2000/svg'><defs><pattern id='a' patternUnits='userSpaceOnUse' width='35' height='30' patternTransform='scale(4) rotate(45)'><rect x='0' y='0' width='100%' height='100%' fill='hsla(0, 0%, 100%, 1)'/><path d='M0 22.5h30v15H0zm15-15h30v15H15m-30-15h30v15h-30zm15-15h30v15H0z' transform='translate(2.5,0)' stroke-width='0.5' stroke='hsla(0, 0%, 0%, 0.23)' fill='none'/></pattern></defs><rect width='800%' height='800%' transform='translate(0,0)' fill='url(%23a)'/></svg>")`,
        calBackGroungColor: '#F7F6DC',
        textColor: 'white',
    }

]
// let pos = 0;
// document.querySelector('.forward').addEventListener('click', ()=>{
//     pos += 1
//     if (pos >= themeArr.length - 1){
//         pos = 0
//     }
    
//     document.querySelector('body').style.backgroundImage = themeArr[pos].backgroundImage
//     document.querySelector('body').style.backgroundImage = 'transparent'
//     document.querySelector('body').style.backgroundColor = themeArr[pos].backgroundColor;
//     document.querySelector('.calculator').style.backgroundColor = themeArr[pos].calBackGroungColor;
//     document.querySelectorAll('button').forEach((element)=>{
//         element.style.backgroundColor = themeArr[pos].buttonBackgroundColor

//     })
// })


// document.querySelector('.backward').addEventListener('click', ()=>{
//     pos -= 1
//     if (pos >= themeArr.length - 1){
//         pos = 0
//     }
//     document.querySelector('body').style.backgroundColor = themeArr[pos].backgroundColor;
//     // document.querySelector('body').style.backgroundImage = themeArr[pos].backgroundImage
//     // document.querySelector('body').style.backgroundImage = 'transparent'
//     document.querySelector('.calculator').style.backgroundColor = themeArr[pos].calBackGroungColor;
//     document.querySelectorAll('button').forEach((element)=>{
//         element.style.backgroundColor = themeArr[pos].buttonBackgroundColor

//     })
// })


// document.querySelector('.forward').addEventListener('click', ()=>(console.log('i just got clicked')))
// $('.forward').click(()=>(console.log('i just got clicked')))

// let button = document.querySelectorAll('button')

// for (let i = 0; i < button.length; i++){
//     button[i].addEventListener('click', ()=>(console.log('i love js')))
// }
let pos = 0
$('.forward').click(()=>{
    pos += 1
    if (pos == themeArr.length - 1){
        pos = 0
    }
    $('body').css('backgroundColor', themeArr[pos].backgroundColor)
    $('.calculator').css('backgroundColor', themeArr[pos].calBackGroungColor)
    $('button').css('backgroundColor', themeArr[pos].buttonBackgroundColor)
})

$('.forward').attr('id', 'forwoar')
console.log($('.forward').attr('id'))
