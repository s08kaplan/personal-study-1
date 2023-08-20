let x = 3;
let y = 5;
let z = x + y;
function mix() {
    let a = (x**2 + y**2)/z;
    return a;
}
console.log(mix());
//-----------------------------------
let a = 3;
let b = 4;
let c = 5;
function mix2(){
    let d = ((a**2 + b**2)*c)**0.5;
    return d;
}
console.log(mix2());
//----------------------
const ab = {
    a: "maria",
    b: "daniel",
    c: "jessica"
}
console.log(ab["a"]);
ab["c"] = "jenny"
console.log(ab["c"]);