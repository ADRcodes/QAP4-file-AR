const motelCustomer = {
  fName: "Alex",
  lname: "Russell",
  birthDate: "1995-09-01",
  gender: "m",
  room_preference: ["101, 102, 107"],
  payment_method: "credit",
  address: {
    street: "1234 Elm St",
    city: "Springfield",
    state: "IL",
    zip: "62701"
  },
  phone: "217-555-5555",
  dates: {
    checkIn: "2021-07-01",
    checkOut: "2021-07-07"
  },
  // object methods to determine their age and duration of stay.
  age: function() {
    const today = new Date();
    const birthDate = new Date(this.birthDate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  },
  duration: function() {
    const checkIn = new Date(this.dates.checkIn);
    const checkOut = new Date(this.dates.checkOut);
    const duration = (checkOut - checkIn) / (1000 * 60 * 60 * 24);
    return duration;
  }
}

document.getElementById("motelCustomer").innerHTML = motelCustomer.fName + " " + motelCustomer.lname + " is " + motelCustomer.age() + " years old and will be staying with us for " + motelCustomer.duration() + " days!" + "<br>" + "<br>" + "<strong>Address: </strong>" + motelCustomer.address.street + ", " + motelCustomer.address.city + ", " + motelCustomer.address.state + " " + motelCustomer.address.zip + "<br>" + "<strong>Phone: </strong>" + motelCustomer.phone + "<br>" + "<strong>Room Preference: </strong>" + motelCustomer.room_preference + "<br>" + "<strong>Payment Method: </strong>" + motelCustomer.payment_method + "<br>" + "<strong>Check In: </strong>" + motelCustomer.dates.checkIn + "<br>" + "<strong>Check Out: </strong>" + motelCustomer.dates.checkOut;

console.log(motelCustomer)