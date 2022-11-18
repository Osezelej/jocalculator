$('button').click(handleClick)
function handleClick (){
    $('button').css('background-color', )
    let weight = $('.weight_input').val()
    let height = $('.height_input').val()

    let BMI = weight / (height * height)
    if (BMI < 18.6){
        $('.results').text('UNDERWEIGHT')
        $('.results').css('color', 'yellow')
        $('.results').css('font-weight', '900')
    }else if(BMI >=18.6 && BMI <= 24.9 ){
        $('.results').text('HEALTHY')
        $('.results').css('color', 'green')
        $('.results').css('font-weight', '900')

    }else{
        $('.results').text('OVERWEIGHT')
        $('.results').css('color', 'red')
        $('.results').css('font-weight', '900')
    }
}

