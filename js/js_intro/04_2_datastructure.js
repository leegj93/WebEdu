// 2. 객체(오브젝트)

const me = {
    name: 'DongWook',
    'phone number': '01022281910',
    appleProducts: {
        ipad: '2018pro',
        iphone: '7+',
        mackbook: '2019pro',
    }
}

me.name // DongWook
me["name"] // DongWook
me["phone number"] // 01022281910

me.appleProducts // { ipad: '2018pro, ....}

// 2-1. Object Literal (ES6+)
// ES5
var books = ['Learning JS', 'Eloquent JS']
var comics = {
    'DC': ['Superman', 'Joker'],
    'Marvel': ['Captain Marvel', 'Avengers'],
}

var magazines = null;

var bookShop = {
    books: books,
    comics: comics,
    magazines: magazines,
}

// ES6
let books = ['Learning JS', 'Eloquent JS']
let comics = {
    'DC': ['Superman', 'Joker'],
    'Marvel': ['Captain Marvel', 'Avengers'],
}

let magazines = null

let bookShop = {
    books,
    comics,
    magazines,
}

// 3. JSON (Javascript Object Notation - JS 객체 표기법)
// Object -> String
const jsonData = JSON.stringify({
    coffee: 'Americano',
    iceCream: 'mint choco',
})

console.log(jsonData) // "{ coffee: 'Americano', iceCream: 'mint choco', }"

// String -> Object
const parsedData = JSON.parse(jsonData)
console.log(parsedData) // { coffee: 'Americano', iceCream: 'mint choco', }
