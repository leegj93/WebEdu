// 03_functions.js

// 1. 선언식 (statement, declaration)
// 코드가 실행되기 전에 로드된다.
function add(num1, num2) {
    return num1 + num2
}

add(2, 7) // 9

// 2. 표현식 (exrpession)
// 인터프리터가 해당 코드에 도달했을 때 로드된다.
const sub = function(num1, num2) {
    return num1 - num2 
}

sub(7, 2) // 5

// 3. Arrow Function
const greeting = function(name) {
    return `hello! ${name}`
}

// 3-1. function 키워드 삭제
const greeting = (name) => { return `hello ${name}` }

// 3-2. () 생략 (매개변수가 하나일 경우에만)
const greeting = name => { return `hello ${name}` }

// 3-3. {} & return 생략 (바디에 표현식이 1일 경우)
const greeting = name => `hello ${name}`

// 4. Anonymous Function (익명함수/1회용)
(function (num) { return num ** 3 })(2) // 8 

