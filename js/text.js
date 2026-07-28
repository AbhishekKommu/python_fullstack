console.log("Hello World")
let student_name = "Abhishek"
console.log("Student name is: " + student_name)
let student_age = 21
let course_name = "Python Full Stack"
console.log("Student age is: " + student_age, "Course name is: " + course_name)
let fee = 10000
let discount = 10
let discount_fee = fee - (fee * discount / 100)
console.log("Discount fee is: " + discount_fee)

let age = 18
age = 20
if (age >= 18) {
    console.log("Eligible for admission")
}
else {
    console.log("Not eligible for admission")
}
for (let i = 1; i <= 5; i++) {
    console.log("Iteration number: " + i)
}
const pi = 3.14

console.log("Value of pi is: " + pi)
let student = {
    name: "Abhi",
    age: 21,
    course: "Python Full Stack",
    fee: 10000
}
console.log("Student details: ", student)

function greetStudent(name) {
    console.log("Hello " + name + ", Welcome ti NRIIT Learning System")
}
greetStudent(student_name)