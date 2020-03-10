/* Collapsible Sidebar Handler */

let sidebar_handler = null;
function Sidebar () {
    const self = this;

    sidebar_handler = self;

    this.service = new CollapsibleElement();
    this.cache = {};
    this.config = {};

    this.trigger_attr_name = 'data-sidebar-toggle';
    this.local_storage_flag = 'sidebar-is-open';
    this.collapse_attr_name = 'collapse_on';

    this.collapse_on_default = 700;

    this.getSidebar = function (sidebar_id) {
        if (!self.cache[sidebar_id]) {
            self.cache[sidebar_id] = $('#' + sidebar_id);
        }
        return self.cache[sidebar_id];
    };

    this.checkState = function (sidebar_id) {
        return self.service.checkState(self.getSidebar(sidebar_id));
    };

    this.getMaxScreenWidth = function (sidebar_id) {
        return self.config[sidebar_id][self.collapse_attr_name] || self.collapse_on_default;
    };

    self.formatSidebarModeKey = function (sidebar_id) {
        return self.local_storage_flag + '-' + sidebar_id;
    };

    this.toggleSidebar = function (sidebar_id) {
        const sidebar_is_open = self.checkState(sidebar_id);

        sidebar_is_open ?
            self.closeSidebar(sidebar_id) :
            self.openSidebar(sidebar_id);
    };

    this.openSidebar = function (sidebar_id) {
        self.service.toggle_(self.getSidebar(sidebar_id), false);
        localStorage.setItem(self.formatSidebarModeKey(sidebar_id), 'true');
        $(document).trigger('collapsible-sidebar:opened', [sidebar_id]);
    };

    this.closeSidebar = function (sidebar_id) {
        self.service.toggle_(self.getSidebar(sidebar_id), true);
        localStorage.setItem(self.formatSidebarModeKey(sidebar_id), 'false');
        $(document).trigger('collapsible-sidebar:closed', [sidebar_id]);
    };

    this.initSignals = function () {
        self.service.initCollapsibleElements();

        $(document).on('click', '[' + self.trigger_attr_name + ']', function (event) {
            /*
            Signal for collapse or expand sidebar.
            */
            const sidebar_id = $(this).attr(self.trigger_attr_name);
            const window_width = $(window).width();

            if (window_width > self.getMaxScreenWidth(sidebar_id)){
                self.toggleSidebar(sidebar_id);
            }

            event.preventDefault();
        });

        $(window).on('resize', function() {
            /*
            Signal for expanding / collapsing the sidebar when resizing the visible area of the screen.
            */
            self.resizeSidebar();
        });
    };

    this.restoreSidebarModeFromCookies = function () {
        $.each(self.config, function (sidebar_id, value) {
            const mode = localStorage.getItem(self.formatSidebarModeKey(sidebar_id));

            if (mode === 'true' || mode === 'false') {
                self.service.toggle_(self.getSidebar(sidebar_id), mode !== 'true');
            }
        });
    };

    this.resizeSidebar = function () {
        const window_width = $(window).width();

        $.each(self.config, function (sidebar_id, value) {
            const screen_width = self.getMaxScreenWidth(sidebar_id);

            if (screen_width && window_width < screen_width) {
                self.service.toggle_(self.getSidebar(sidebar_id), true);
            }
        });
    }
}
