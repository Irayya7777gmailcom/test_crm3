const otherCheckbox = document.getElementById('otherCheckbox');
const otherText = document.getElementById('otherText');

otherCheckbox.addEventListener('change', function () {
    otherText.disabled = !otherCheckbox.checked;
});

var employeeDiv=document.getElementById('client_level')
var levelofLead=document.getElementById('client_level_of_lead')
var clientSource=document.getElementById('client_source')
var clientOtherSource=document.getElementById('client_other_source')
var CourseEnquired=document.getElementById('course_enquired')
var OtherCourseEnquired=document.getElementById('client_other_course_enquired')


levelofLead.addEventListener('change', function () {
  if (levelofLead.value === 'Employee') {
    employeeDiv.style.display = 'block';
  } else {
    employeeDiv.style.display = 'none';
  }
});

clientSource.addEventListener('change', function () {
  if (clientSource.value === 'Other') {
    clientOtherSource.style.display = 'block';
    clientSource.setAttribute('name',"empty")
    console.log(clientSource.getAttribute('name'))
  } else {
    clientOtherSource.style.display = 'none';
    clientSource.setAttribute('name',"source")
    console.log(clientSource.getAttribute('name'))
  }
});

CourseEnquired.addEventListener('change', function () {
  if (CourseEnquired.value === 'Other') {
    OtherCourseEnquired.style.display = 'block';
    CourseEnquired.setAttribute('name',"empty")
    console.log(CourseEnquired.getAttribute('name'))
  } else {
    OtherCourseEnquired.style.display = 'none';
    CourseEnquired.setAttribute('name',"course_enquired")
    console.log(CourseEnquired.getAttribute('name'))
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
  const stateSelect = document.getElementById("client_state");
  const citySelect = document.getElementById("client_city");
  const selectedState = stateSelect.value;
  
  citySelect.innerHTML = "";

  for (const city of stateCities[selectedState]) {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
  }
}


function filterCompanyCities(){
  const companyStateSelect = document.getElementById("client_company_state");
  const companyCitySelect = document.getElementById("client_company_city");
  const selectedState = companyStateSelect.value;
  
  companyCitySelect.innerHTML = "";

  for (const city of stateCities[selectedState]) {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      companyCitySelect.appendChild(option);
  }
}

const DegreeSpecification = {
  "Bsc": ["CS","Biology","Chemistry","Physics","Maths","Statistics","Environmental Science","Geology"],
  "BE": ["CS","Electrical","Civil","Mechanical","Biomedical","Aerospace"],
  "BBA": ["Marketing","Finance","Management","Accounting","Entrepreneurship","HR Management","International Business"],
  "BCA": ["Computer Applications","Software Development"],
  "B-Tech": ["CS","Electrical","Civil","Mechanical","Biomedical","Aerospace"],
  "BCom": ["Marketing","Finance","Management","Accounting","Entrepreneurship","HR Management","International Business"],

  "Msc": ["CS","Biology","Chemistry","Physics","Maths","Statistics","Environmental Science","Geology"],
  "ME": ["CS","Electrical","Civil","Mechanical","Biomedical","Aerospace"],
  "MBA": ["Marketing","Finance","Management","Accounting","Entrepreneurship","HR Management","International Business"],
  "MCA": ["Computer Applications","Software Development"],
  "M-Tech": ["CS","Electrical","Civil","Mechanical","Biomedical","Aerospace"],
  "MS":["CS","Biotechnology","Environmental Science","Economics","Data Science"],
  "MCom": ["Marketing","Finance","Management","Accounting","Entrepreneurship","HR Management","International Business"]
};

function BachelorSpecification(){
  const bachelorDegree=document.getElementById('bachelor_degree').value
  const bachelorSpecification=document.getElementById('bachelor_specification')

  bachelorSpecification.innerHTML=""
  degree(bachelorDegree,bachelorSpecification)
}

function MastersSpecification(){
  const masterDegree = document.getElementById("master_degree").value;
  const masterSpecification = document.getElementById("master_specification");
  
  masterSpecification.innerHTML = "";
  degree(masterDegree,masterSpecification)
}

function degree(x,y){
  for(const specification of DegreeSpecification[x]){
    const option=document.createElement("option")
    option.value=specification
    option.textContent=specification
    y.appendChild(option)
  }
}

filterCompanyCities();
filterCities();

function validateForm() {
  var Contact = document.getElementById('contact_number').value;
  var CompanyContact = document.getElementById('company_contact_number').value;
  var companyGstNumber=document.getElementById('company_gstnumber').value;
  var pincode=document.getElementById('pincode').value;
  var companyPincode=document.getElementById('company_pincode').value;
  var website=document.getElementById('comapny_website').value;

  document.getElementById('contactNumberError').innerHTML = '';
  document.getElementById('companyContactNumberError').innerHTML = '';
  document.getElementById('gstNumberError').innerHTML = '';
  document.getElementById('pincodeError').innerHTML = '';
  document.getElementById('companypincodeError').innerHTML = '';
  document.getElementById('websiteError').innerHTML='';

  var phonePattern1 = /^[6789]\d{9,9}$/g;
  var phonePattern2 = /^[6789]\d{9,9}$/g;
  var gstPattern = /^[0-9]{2}[0-9A-Z]{10}[0-9]{1}[A-Z]{1}[0-9]{1}$/;
  var pincodePattern=/^[1-9]{1}[0-9]{2}[0-9]{3}$/;
  var websitePattern=/[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;

  if (!phonePattern1.test(Contact)) {
      document.getElementById('contactNumberError').innerHTML = 'Enter The Valid Contact Number';
      return false;
  }

  if (!phonePattern2.test(CompanyContact)) {
      document.getElementById('companyContactNumberError').innerHTML = 'Enter The Valid Contact Number';
      return false;
  }
  if (!gstPattern.test(companyGstNumber)) {
      document.getElementById('gstNumberError').innerHTML = 'Enter The Valid GST Number';
      return false;
  }
  if (!pincodePattern.test(pincode)) {
      document.getElementById('pincodeError').innerHTML = 'Enter The Valid Pincode Number';
      return false;
  }
  if (!pincodePattern.test(companyPincode)) {
      document.getElementById('companypincodeError').innerHTML = 'Enter The Valid Pincode Number';
      return false;
  }
  if (!websitePattern.test(website)) {
      document.getElementById('websiteError').innerHTML = 'Enter The Valid Website URL';
      return false;
  }

  return true
}





