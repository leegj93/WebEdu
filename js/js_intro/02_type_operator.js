// 02_type_operator.js

// Primitivie 타입
// 1. Numbers
const a = 13
const b = -5
const c = 3.14 // float
const d = 2.998e8
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number. ex) 0/0, "문자"*10 

// 2. String
const sentence1 = 'Ask and go to the blue' // single quote
const sentence2 = "Ask and go to the blue" // double quote
const sentence3 = `Ask and go to the blue` // backtic

// 2-1. 줄바꿈
// const word = "안녕
// 하세요"

const word1 = "안녕 \n하세요" 
console.log(word1)

// 2-2. 리터럴
const word2 = `안녕
하세요`
console.log(word2)

const age = 10
const message = `홍길동은 ${age}`
console.log(message)

const hacking = 'Happy' + 'Hacking' + '!'
console.log(hacking)

// 3. Boolean
true
false

// 4. Empty Value
let first_name
console.log(first_name) // undefined 

let last_name = null
console.log(last_name) // null

typeof null // object
typeof undefined // undefined

// 연산자
// 1. 할당 연산자
let c = 0 

c += 10 
console.log(c) // 10 - C에 10을 더한다. 

c -= 3
console.log(c) // 7 - C에 3을 뺀다. 

c *= 10
console.log(c) // 70 - c에 10을 곱한다.

c++
console.log(c) // 71 - c에 1을 더한다. 

c-- 
console.log(c) // 70 - c에 1을 뺀다. 

// 2. 비교 연산자
// (*참고) 변수 앞에 var, const, let을 붙여주지 않으면
// JS엔진이 자동으로 var를 붙여준다.
3 > 2 // true
3 < 2 // false

'A' < 'B' // true
'Z' < 'a' // true
'가' < '나' // true

// 3. 동등 연산자 (동등 연산자의 사용은 지.양.한다.)
const a = 1
const b = '1'

console.log(a == b) // true
console.log(a != b) // false

// 4. 일치 연산자
console.log(a === b) // false
console.log(a === Number(b)) // true

// 5. 논리 연산자 (and, or, not)
true && false // false
ture && true // true

1 && 0 // 0
0 && 1 // 0
4 && 7 // 7

false || true // true
false || false // false

1 || 0 // 1
0 || 1 // 1
4 || 7 // 4

!true // false

// 6. 삼항 연산자 (Ternary Operator)
true ? 1 : 2 // 1
false ? 1: 2 // 2
'justin' ? 'nice' : 'awesome' // 'nice'

// 조건문과 반복문
// 1. if문
const userName = prompt("Hello! Who are you?")

let message = ''

if (userName === '1q2w3e4r') {
    message = "<h1>This is Secret Admin Page</h1>"
} else if (userName === 'Kang') {
    message = "<h1>Hello, Kang!</h1>"
} else {
    message = `<h1>Hello, ${userName}</h1>`
}

console.log(message)

// 2. switch 문
const userName = prompt("Hello, who are you?")

let message = ''

switch(userName) {
    case '1q2w3e4r': {
        message = "<h1>This is Secret Admin Page</h1>"
        break
    }
    case 'Kang': {
        message = '<h1>Hello, Kang!</h1>'
        break
    }
    default: {
        message = `<h1>Hello, ${userName}</h1>`
    }
}

// 반복문
// 1. while loop
let i = 0

while (i < 6) {
    console.log(i)
    i++
}

// 2. for loop
for (let j = 0; j < 6; j++) {
    console.log(j)
}

const numbers = [0, 1, 2, 3, 4, 5]

for (let number of numbers) {
    console.log(number)
}