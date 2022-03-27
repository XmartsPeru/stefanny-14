/**
Part of Odoo Module Developed by Cloudia S.A.C. | http://cloudia.solutions | <info@cloudia.solutions>
Copyright (c) 2021 Cloudia S.A.C.
See LICENSE and COPYRIGHT files for full copyright and licensing details.
*/

odoo.define('web_xmpe.FormController', function (require) {
    'use strict'

    var FormController = require('web.FormController');
    FormController.include({
        start: function () {
            this.$el.addClass('o_form_controller');
            return this._super.apply(this, arguments);
        }
    })
});
