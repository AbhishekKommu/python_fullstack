alert("Welcome to NRIIT learning Management System");
let heading = document.getElementById("welcome");
heading.innerHTML = "Welcome Future Software Engineers";
console.log("Heading element: ", heading);
let msg = document.getElementById("message");
msg.innerHTML = "Javascript is fun";
console.log("Message element: ", msg);
function showmessage() {
    alert("Welcome to NRIIT Learning Management System");
}
function ChangeHeading() {
    document.getElementById("welcome").innerHTML = "Welcome Full Stack Developer"
}
heading = document.querySelector("#welcome");
console.log("Heading element: ", heading);
let button = document.getElementById("btnGreeting");
button.addEventListener("click", function () {
    alert("Welcome to javacript Event Handling");
});
let registaredForm = document.getElementById("registerForm");
registaredForm.addEventListener("submit", function (event) {
    event.preventDefault();
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    if (!name || !email || !password ){alert("please fill in all fields");
        return;
    }
    alert("Registration sucessfully!")
})
