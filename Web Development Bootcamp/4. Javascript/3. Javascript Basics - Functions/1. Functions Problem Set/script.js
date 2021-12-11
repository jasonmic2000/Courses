console.log("Printing Even Numbers")

function isEven(number) {
    if(number % 2 === 0) {
        console.log(number + " is even.");
    }
    else {
        console.log(number + " is not even.");
    }
}

console.log("Printing Factorials")

function factorial(fact) {
    var result = fact
    for(var i = fact-1; i > 0; i--) {
        result = result * i;
    }
    return result;
}


console.log("Kebab to Snake Casing")

function kebabToSnake(str) {
    // replaces all '-' with '_'s

    newstr = str.replace(/-/g,"_");
    //return str
    return newstr;
}