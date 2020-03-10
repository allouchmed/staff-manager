// Container functions

const staff_manager = {
    initSidebar: function () {
        /*
        Function for sidebar initialization.
        */

        const sidebar_handler = new Sidebar();
        sidebar_handler.config = {
            'main_sidebar': {
                'collapse_on': 700
            }
        };
        sidebar_handler.initSignals();
        sidebar_handler.resizeSidebar();

        $(document).on('collapsible-sidebar:opened collapsible-sidebar:closed', function (event, sidebar_id) {
            const state = sidebar_handler.checkState(sidebar_id);
            const url = '/utils/sidebar-mode/save/' + sidebar_id + '/' + state + '/';

            $.ajax(url);
            event.preventDefault();
        });
    },

    initFormSubmitButton: function () {
        $(document).on('click', '[data-form-submit]', function (event) {
            const form_id = $(this).data('form-submit');
            const form = $(form_id);

            event.preventDefault();
            form.submit();

        })

    },

    initPerfectScrollbar: function (scroll_element_selector) {
        if ($(scroll_element_selector).length) {
            new PerfectScrollbar(scroll_element_selector);
        }
    },

    initAlerts: function() {
        $(document).on('click', '.js-alert_dismiss_btn', function (event) {
            const alert_block = $(this).closest('.js-alert_block');

            alert_block.fadeOut(300, function() {
                alert_block.remove();
            });
            event.preventDefault();
        })
    },

    initFilterForms: function () {
        $(document).on('change', '.js-filter_form', function (event) {

            $(this).submit();
            event.preventDefault();
        })
    },

    initTableItemsSelection: function () {
        $(document).on('click', '.js-table_item_add, .js-table_item_delete', function (event) {
            const btn = $(this);
            const url = btn.data('url');
            const item_add_icon = btn.closest('tr').find('.js-table_item_add_icon');
            const item_delete_icon = btn.closest('tr').find('.js-table_item_delete_icon');

            btn.hasClass('js-table_item_add') ?
                item_add_icon.toggleClass('active') :
                item_delete_icon.toggleClass('active');

            $.ajax(url);
            event.preventDefault();
        })
    },

    initFloatingWindows: function () {
        const fw = new FloatingWindows();
        fw.config = {
            'confirm_action': {
                'floatingWindowTitle': 'Confirm action',
                'floatingWindowPosition': '30%,40%',
                'floatingWindowSetBackground': 'body',
                'floatingWindowShowFooter':  false,
            }
        };
        fw.initWindows();

        $(document).on('floating-window:opened', function (event, window, trigger) {
            const window_id = window.attr('id');
            let url = trigger.data('url');
            let container = window.find(fw.windows_body_selector).find(':first');

            switch (window_id) {
                case 'confirm_action' :
                    const confirmation_id = trigger.data('confirmation-id');
                    let message = 'Data will be lost!';
                    let subject = confirmation_id.charAt(0).toUpperCase() + confirmation_id.slice(1);
                    let message_title = 'Confirm ' + subject + ' instance deletion!';

                    switch (confirmation_id) {
                        case 'employees_selection':
                            message_title = 'Confirm Employees selection!';
                            message = '';
                            break;
                        case 'employees_selection_flush':
                            message_title = 'Confirm Employees selection flush!';
                            message = '';
                            break;
                        default:
                            break;
                    }

                    container.find('form').attr('action', url);
                    container.find('.js-confirmation_title').html(message_title);
                    container.find('.js-confirmation_message').html(message);
                    break;
                default:
                    break;
            }
        });
    }
};