const stars = document.querySelectorAll('.star');
const priorityValue = document.getElementById('priority-value');

stars.forEach(star => {
  star.addEventListener('click', () => {
    const value = parseInt(star.getAttribute('data-value'));

    stars.forEach(s => {
      s.classList.remove('active');
    });

    for (let i = 0; i < value; i++) {
      stars[i].classList.add('active');
    }

    priorityValue.innerText = value;
  });
});

const otherCheckbox = document.getElementById('otherCheckbox');
const otherText = document.getElementById('otherText');

otherCheckbox.addEventListener('change', function () {
    otherText.disabled = !otherCheckbox.checked;
});

var employeeDiv=document.getElementById('customer_level')
var levelofLead=document.getElementById('customer_level_of_lead')
var customerSource=document.getElementById('customer_source')
var customerOtherSource=document.getElementById('customer_other_source')

          levelofLead.addEventListener('change', function () {
  if (levelofLead.value === 'Employee') {
    employeeDiv.style.display = 'block';
  } else {
    employeeDiv.style.display = 'none';
  }
});

customerSource.addEventListener('change', function () {
  if (customerSource.value === 'Other') {
    customerOtherSource.style.display = 'block';
  } else {
    customerOtherSource.style.display = 'none';
  }
});


const stateCities = {
    "Andhra Pradesh": ["Hyderabad", "Visakhapatnam", "Vijayawada", "Guntur", "Nellore"],
    "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Nagaon"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Purnia"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Durg", "Bilaspur", "Korba"],
    "Goa": ["Panaji", "Margaon", "Vasco da Gama"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar"],
    "Haryana": ["Chandigarh", "Faridabad", "Gurgaon", "Hisar", "Panipat"],
    "Himachal Pradesh": ["Shimla", "Mandi", "Dharamshala", "Solan"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh"],
    "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kollam"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Thane", "Nashik"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
    "Meghalaya": ["Shillong", "Tura", "Nongstoin"],
    "Mizoram": ["Aizawl", "Lunglei", "Serchhip"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur", "Puri"],
    "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner"],
    "Sikkim": ["Gangtok", "Namchi", "Mangan"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Khammam", "Karimnagar"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Meerut"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Rishikesh", "Haldwani"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri"]
};


function filterCities() {
    const stateSelect = document.getElementById("customer_state");
    const citySelect = document.getElementById("customer_city");
    const selectedState = stateSelect.value;
    
    citySelect.innerHTML = "";
    

    for (const city of stateCities[selectedState]) {
        const option = document.createElement("option");
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
    }
}

filterCities();


