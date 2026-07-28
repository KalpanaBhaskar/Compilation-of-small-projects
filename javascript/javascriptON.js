// Create an object (JSON-like object)
let obj = {
    id: 101,
    name: "Alice",
    age: 22,
    city: "Chennai"
};

console.log("Original Object:");
console.log(obj);

// -------------------------
// Copy the object
// -------------------------
let copyObj = { ...obj };      // Spread operator
// OR: let copyObj = Object.assign({}, obj);

console.log("\nCopied Object:");
console.log(copyObj);

// -------------------------
// Add a new property
// -------------------------
obj.course = "JavaScript";
obj.marks = 95;

console.log("\nAfter Adding Properties:");
console.log(obj);

// -------------------------
// Update a property
// -------------------------
obj.age = 23;

console.log("\nAfter Updating Age:");
console.log(obj);

// -------------------------
// Delete a property
// -------------------------
delete obj.city;

console.log("\nAfter Deleting 'city':");
console.log(obj);

// -------------------------
// Display using for...in loop
// -------------------------
console.log("\nDisplay using for...in:");
for (let key in obj) {
    console.log(key + " : " + obj[key]);
}

// -------------------------
// Display using Object.keys()
// -------------------------
console.log("\nUsing Object.keys():");
Object.keys(obj).forEach(key => {
    console.log(key + " : " + obj[key]);
});

// -------------------------
// Display using Object.values()
// -------------------------
console.log("\nUsing Object.values():");
Object.values(obj).forEach(value => {
    console.log(value);
});

// -------------------------
// Display using Object.entries()
// -------------------------
console.log("\nUsing Object.entries():");
Object.entries(obj).forEach(([key, value]) => {
    console.log(key + " : " + value);
});

// -------------------------
// Convert object to JSON string
// -------------------------
let jsonString = JSON.stringify(obj);

console.log("\nJSON String:");
console.log(jsonString);

// Pretty JSON format
console.log("\nPretty JSON:");
console.log(JSON.stringify(obj, null, 2));

// -------------------------
// Convert JSON string back to object
// -------------------------
let parsedObj = JSON.parse(jsonString);

console.log("\nParsed Object:");
console.log(parsedObj);