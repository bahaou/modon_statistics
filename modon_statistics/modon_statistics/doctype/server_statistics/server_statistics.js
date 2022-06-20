// Copyright (c) 2022, baha and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Statistics', {
	 refresh: function(frm) {
		frm.add_custom_button(__("Sync"), function() {
     			frappe.call({
				method: "modon_statistics.modon_statistics.doctype.server_statistics.server_statistics.sync",
				args: {"server":frm.doc.name},
				freeze: true,
				freeze_message: "Please wait...",
				callback: function() {
					frm.refresh();
					
					frappe.msgprint("Updated Statistics Succesfully.")
				},
			});
		






   		 });
		frm.add_custom_button(__("Visit Website"), function() {
     			window.open(frm.doc.url, "_blank");
   		 });
		frm.add_custom_button(__("Open rdp"), function() {
     			window.open(frm.doc.rdp, "_blank");
   		 });

	}
});
