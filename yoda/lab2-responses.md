Yoda Chat: Responses
================

B. Inspect Mode
---------------
1) chocolate

2) next_week = "Guest talk?"

3) fonts.googleapis.com

C. Welcome to Programming in Javascript
---------------------------------------
3) y.includes("hello") only returns true when the string includes "hello", while y.repeat(10) repeats our string 10 times concatenated.

4) square(2.5) returns 6.25, while square("hello") returns NaN.

5)
function square(i) {
  if(typeof i == "number") {
    return i*i
    } else {
      return -1
      }
}

6)
function numberString(i) {
  if(i % 1 == 0 && typeof i == "number") {
    let result = ""
    for (let j = 0; j < i; j++) {
        result += j
    }
    return result
  }
  else {
    return -1
  }
}

