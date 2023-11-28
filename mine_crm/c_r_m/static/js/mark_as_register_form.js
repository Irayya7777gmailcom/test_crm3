const selectElement = document.getElementById('registered-mode_of_payment');
const Chequediv = document.getElementById('cheque-payment');
const UPIdiv = document.getElementById('upi-payment');
const DDdiv=document.getElementById('DD-payment')
const BankTransferdiv=document.getElementById('Bank-transfer')
const cashdiv=document.getElementById('cash-payment')

selectElement.addEventListener('change', function () {
  if (selectElement.value === 'Cheque') {
    Chequediv.style.display = 'block';
  } else {
    Chequediv.style.display = 'none';
  }
});

selectElement.addEventListener('change', function () {
  if (selectElement.value === 'UPI') {
    UPIdiv.style.display = 'block';
  } else {
    UPIdiv.style.display = 'none';
  }
});
selectElement.addEventListener('change', function () {
  if (selectElement.value === 'DD') {
    DDdiv.style.display = 'block';
  } else {
    DDdiv.style.display = 'none';
  }
});
selectElement.addEventListener('change', function () {
  if (selectElement.value === 'Bank Transfer') {
    BankTransferdiv.style.display = 'block';
  } else {
    BankTransferdiv .style.display = 'none';
  }
});
selectElement.addEventListener('change', function () {
  if (selectElement.value === 'Cash') {
    cashdiv.style.display = 'block';
  } else {
    cashdiv .style.display = 'none';
  }
});

const five_hundred=document.getElementById('500_quantity')
const two_hundred=document.getElementById('200_quantity')
const hundred=document.getElementById('100_quantity')
const fifty=document.getElementById('50_quantity')
const twenty=document.getElementById('20_quantity')
const ten=document.getElementById('10_quantity')

const five_hundred_total=document.getElementById('500_total')
const two_hundred_total=document.getElementById('200_total')
const hundred_total=document.getElementById('100_total')
const fifty_total=document.getElementById('50_total')
const twenty_total=document.getElementById('20_total')
const ten_total=document.getElementById('10_total')

five_hundred.addEventListener('input',()=>{
  var quantity=five_hundred.value
  individual_total(500,quantity,five_hundred_total)
})
two_hundred.addEventListener('input',()=>{
  var quantity=two_hundred.value
  individual_total(200,quantity,two_hundred_total)
})
hundred.addEventListener('input',()=>{
  var quantity=hundred.value
  individual_total(100,quantity,hundred_total)
})
fifty.addEventListener('input',()=>{
  var quantity=fifty.value
  individual_total(50,quantity,fifty_total)
})
twenty.addEventListener('input',()=>{
  var quantity=twenty.value
  individual_total(20,quantity,twenty_total)
})
ten.addEventListener('input',()=>{
  var quantity=ten.value
  individual_total(10,quantity,ten_total)
})
function individual_total(note,quantity,x){
var total=note*quantity;
x.textContent="₹"+total
}

