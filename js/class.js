// Your code here.
class Vec {
  constructor(x,y) {
    this.x = x;
    this.y = y;
  }
  get length() {
    return Math.sqrt(this.x*this.x + this.y*this.y);
  }
  plus(vc) {
    return new Vec(this.x + vc.x, this.y + vc.y);
  }
  minus(vc) {
    return new Vec(this.x - vc.x, this.y - vc.y);
  }
}
console.log("Hello");
console.log(new Vec(1, 2).plus(new Vec(2, 3)));
// → Vec{x: 3, y: 5}
console.log(new Vec(1, 2).minus(new Vec(2, 3)));
// → Vec{x: -1, y: -1}
console.log(new Vec(3, 4).length);
// → 5

class Group {
  constructor(){
    this.group=[];
  }
  add(value) {
    if ( ! this.group.includes(value) ) {
         this.group.push(value);
     }
  }
  del(value) {
    let newgroup=[]
    if ( this.group.includes(value) ) {
         newgroup = this.group.filter(x => {if (x != value) return x});
         this.group = newgroup;
     }
  }

  has(value) {
     return this.group.includes(value);
  }

  static From(arr) {
   let newGr = new Group();
   for (var index in arr) {
       newGr.add(arr[index]);
    }
   return newGr;
  }
}

let group = Group.From([10, 20]);
console.log(group.has(10));
// → true
console.log(group.has(30));
// → false
group.add(10);
group.delete(10);
console.log(group.has(10));


class Temperature {
  constructor(celsius) {
    this.celsius = celsius;
  }
  get fahrenheit() {
    return this.celsius * 1.8 + 32;
  }
  set fahrenheit(value) {
    this.celsius = (value - 32) / 1.8;
  }

  static fromFahrenheit(value) {
    return new Temperature((value - 32) / 1.8);
  }
}

let temp = new Temperature(22);
console.log(temp.fahrenheit);
// → 71.6
temp.fahrenheit = 86;
console.log(temp.celsius);
// → 30
