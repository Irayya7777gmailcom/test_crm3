
    // Get references to the buttons and content divs
const newLeadsbutton = document.getElementById("clientnewleads-btn");
const followupLeadsbutton = document.getElementById("clientfollowupleads-btn");
const prospectsbutton = document.getElementById("clientprospects-btn");
const registeredbutton = document.getElementById("clientregistered-btn");
const closedbutton = document.getElementById("clientclosed-btn");

const newLeadsTable_div = document.getElementById("clientnewLeadsTable");
const followupLeadsTable_div = document.getElementById("clientfollowupLeadsTable");
const prospectsTable_div = document.getElementById("clientprospectsTable");
const registeredTable_div = document.getElementById("clientregisteredTable");
const closedTable_div = document.getElementById("clientclosedTable");


newLeadsbutton.addEventListener("click", () => {
    newLeadsTable_div.style.display = "block";
    followupLeadsTable_div.style.display = "none";
    prospectsTable_div.style.display = "none";
    registeredTable_div.style.display = "none";
    closedTable_div.style.display = "none";
});
followupLeadsbutton.addEventListener("click", () => {
    newLeadsTable_div.style.display = "none";
    followupLeadsTable_div.style.display = "block";
    prospectsTable_div.style.display = "none";
    registeredTable_div.style.display = "none";
    closedTable_div.style.display = "none";
});
prospectsbutton.addEventListener("click", () => {
    newLeadsTable_div.style.display = "none";
    followupLeadsTable_div.style.display = "none";
    prospectsTable_div.style.display = "block";
    registeredTable_div.style.display = "none";
    closedTable_div.style.display = "none";
});
registeredbutton.addEventListener("click", () => {
    newLeadsTable_div.style.display = "none";
    followupLeadsTable_div.style.display = "none";
    prospectsTable_div.style.display = "none";
    registeredTable_div.style.display = "block";
    closedTable_div.style.display = "none";
});
closedbutton.addEventListener("click", () => {
    newLeadsTable_div.style.display = "none";
    followupLeadsTable_div.style.display = "none";
    prospectsTable_div.style.display = "none";
    registeredTable_div.style.display = "none";
    closedTable_div.style.display = "block";
});


