// Components initialization.

$(document).ready(function () {
    // Sidebar
    staff_manager.initSidebar();
    // Forms submit
    staff_manager.initFormSubmitButton();
    // Perfect Scrollbar
    staff_manager.initPerfectScrollbar('.js-perfect_scrollbar');
    // Floating Windows
    staff_manager.initFloatingWindows();
    // Custom Alerts
    staff_manager.initAlerts();
    // Filter Forms
    staff_manager.initFilterForms();
    // Table selection
    staff_manager.initTableItemsSelection();

    // Waves Effects
    Waves.attach('.waves-btn', ['waves-button']);
    Waves.init();
});