let objdemo = {
    name:"Alice",age :30,city:"new york"
};
console.log(objdemo.name);
console.log(objdemo.age);
console.log(Object.values(objdemo));
console.log(JSON.stringify(objdemo));
for (let key in objdemo){
    console.log(key+" : "+ objdemo[key]);
}
objdemo.Position=("Doctor");
for (let key in objdemo){
    console.log(key+" : "+ objdemo[key]);
}