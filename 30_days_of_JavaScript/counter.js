var createCounter = function(n) {

    return function() {{
        let result = n;
        n++;
        return result;
    }}
}

const counter1 = createCounter(20);

console.log(counter1);