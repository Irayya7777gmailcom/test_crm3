const customernewLeadsbutton = document.getElementById("customernewleads-btn");
const customerfollowupLeadsbutton = document.getElementById("customerfollowupleads-btn");
const customerprospectsbutton = document.getElementById("customerprospects-btn");
const customerregisteredbutton = document.getElementById("customerregistered-btn");
const customerclosedbutton = document.getElementById("customerclosed-btn");

const customernewLeadsTable_div = document.getElementById("customernewLeadsTable");
const customerfollowupLeadsTable_div = document.getElementById("customerfollowupLeadsTable");
const customerprospectsTable_div = document.getElementById("customerprospectsTable");
const customerregisteredTable_div = document.getElementById("customerregisteredTable");
const customerclosedTable_div = document.getElementById("customerclosedTable");


customernewLeadsbutton.addEventListener("click", () => {
    customernewLeadsTable_div.style.display = "block";
    customerfollowupLeadsTable_div.style.display = "none";
    customerprospectsTable_div.style.display = "none";
    customerregisteredTable_div.style.display = "none";
    customerclosedTable_div.style.display = "none";
});
customerfollowupLeadsbutton.addEventListener("click", () => {
    customernewLeadsTable_div.style.display = "none";
    customerfollowupLeadsTable_div.style.display = "block";
    customerprospectsTable_div.style.display = "none";
    customerregisteredTable_div.style.display = "none";
    customerclosedTable_div.style.display = "none";
});
customerprospectsbutton.addEventListener("click", () => {
    customernewLeadsTable_div.style.display = "none";
    customerfollowupLeadsTable_div.style.display = "none";
    customerprospectsTable_div.style.display = "block";
    customerregisteredTable_div.style.display = "none";
    customerclosedTable_div.style.display = "none";
});
customerregisteredbutton.addEventListener("click", () => {
    customernewLeadsTable_div.style.display = "none";
    customerfollowupLeadsTable_div.style.display = "none";
    customerprospectsTable_div.style.display = "none";
    customerregisteredTable_div.style.display = "block";
    customerclosedTable_div.style.display = "none";
});
customerclosedbutton.addEventListener("click", () => {
    customernewLeadsTable_div.style.display = "none";
    customerfollowupLeadsTable_div.style.display = "none";
    customerprospectsTable_div.style.display = "none";
    customerregisteredTable_div.style.display = "none";
    customerclosedTable_div.style.display = "block";
});


