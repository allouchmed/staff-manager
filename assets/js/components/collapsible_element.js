/* Collapsible Element handler */


let collapsible_element_handler = null;
function CollapsibleElement() {
    const self = this;

    collapsible_element_handler = self;

    this.element_is_open_class = 'is-open';
    this.element_closed_class = 'closed';
    this.element_state_attr_name = 'data-is-open';

    this.initCollapsibleElements = function () {
        $('[' + self.element_state_attr_name + '="true"]').addClass(self.element_is_open_class);
        $('[' + self.element_state_attr_name + '="false"]').addClass(self.element_closed_class);
    };

    this.toggleCollapsibleElementByTrigger = function (trigger, collapsible_element_selector) {
        const element = $(trigger).closest(collapsible_element_selector);
        self.toggle_(element);
    };

    this.checkState = function (element_object) {
        return element_object.hasClass(self.element_is_open_class);
    };

    this.toggle_ = function(element_object, state_to_close=null) {
        if (state_to_close === null && element_object.hasClass(self.element_is_open_class) || state_to_close) {
            element_object.removeClass(self.element_is_open_class);
            element_object.attr(self.element_state_attr_name, false);
            return false;
        }
        else {
            element_object.addClass(self.element_is_open_class);
            element_object.attr(self.element_state_attr_name, true);
            return true;
        }
    };

    this.initSignals = function (collapsible_element_selector, trigger_selector) {
        $(document).on('click', trigger_selector, function (e) {
            self.toggleCollapsibleElementByTrigger($(this), collapsible_element_selector);
        });
    }
}