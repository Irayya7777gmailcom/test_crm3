document.addEventListener("DOMContentLoaded", function() {
    const dataTable = document.getElementById("newLeadsModal");
    const modal = document.getElementById("prospectsModal");
    const modalId = document.getElementById("lead_id");
    const openModalButtons = document.querySelectorAll(".open-modal");
    
    function openModal(id) {
        modalId.value = id;
        modal.style.display = "block";
    }
    
    function closeModal() {
        modal.style.display = "none";
    }
    
    dataTable.addEventListener("click", function(event) {
        if (event.target.tagName === "BUTTON" && event.target.classList.contains("open-modal")) {
            const row = event.target.closest("tr");
            const idCell=row.querySelector('.row_id')
            const id=idCell.textContent
            openModal(id);
        }
    });
    
    const closeModalButton = document.getElementById("close-modal");
    closeModalButton.addEventListener("click", closeModal);
    });