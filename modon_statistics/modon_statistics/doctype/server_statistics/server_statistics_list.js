frappe.listview_settings["Server Statistics"] = {

	onload: function(listview) {
		listview.page.add_menu_item(__("synchronize"), function() {
			frappe.call({
				method: "modon_statistics.modon_statistics.doctype.server_statistics.server_statistics.sync",
				freeze: true,
				freeze_message: "Please wait...",
				callback: function() {
					listview.refresh();
					frappe.msgprint("Updated Statistics Succesfully.");
				},
			});
		});

		
	},
};
