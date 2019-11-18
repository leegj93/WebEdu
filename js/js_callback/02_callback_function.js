const numbersEach = (numbers, callback) => {
    let acc // accumulator
    for (const number of numbers) {
        acc = callback(number, acc) // [???]한다 === callback
    }
    return acc
}

// 더한다
const addEach = (number, acc = 0) => {
    return acc + number
}

// 뺀다
const subEach = (number, acc = 0) => {
    return acc - number
}

// 곱한다
const mulEach = (number, acc = 1) => {
    return acc * number
}

const NUMBERS = [1, 2, 3, 4, 5]
console.log(numbersEach(NUMBERS, addEach))
console.log(numbersEach(NUMBERS, subEach))
console.log(numbersEach(NUMBERS, mulEach))

