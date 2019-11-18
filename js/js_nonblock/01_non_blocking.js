// function sleep_3s() {
//     setTimeout(() => console.log('Wake up!'), 3000)
// }cd

// console.log('Start Sleeping')
// sleep_3s()
// console.log("End of Program!")

function first() {
    console.log('first')
}

function second() {
    console.log('second')
}

function third() {
    console.log('third')
}

first()
setTimeout(second, 0)
third()
