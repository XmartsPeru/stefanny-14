/**
Part of Odoo Module Developed by Cloudia S.A.C. | http://cloudia.solutions | <info@cloudia.solutions>
Copyright (c) 2021 Cloudia S.A.C.
See LICENSE and COPYRIGHT files for full copyright and licensing details.
*/

odoo.define('web_xmpe.PivotController', function (require) {
    'use strict'
    var PivotController = require('web.PivotController')
    PivotController.include({
        start: function () {
            this.$el.addClass('o_pivot_controller');
            return this._super.apply(this, arguments);
        }
    })
});
