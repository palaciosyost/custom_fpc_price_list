/** @odoo-module **/
import { registry } from "@web/core/registry";
import { onMounted } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";

function setupStockInfoButton(env) {
    onMounted(() => {
        document.querySelectorAll(".js_stock_info_button").forEach(btn => {
            btn.addEventListener("click", async (ev) => {
                const tr = ev.currentTarget.closest("tr");
                const lineId = parseInt(tr?.getAttribute("data-id"));
                if (!lineId) return;

                try {
                    const result = await env.services.rpc("/stock_info_from_line", {
                        line_id: lineId,
                    });

                    new Dialog(env, {
                        title: "Información de Stock",
                        size: "medium",
                        body: `
                            <div style="padding: 10px;">
                                <p><strong>Existencias pronosticadas:</strong> ${result.forecasted_qty}</p>
                                <p><strong>Disponibles:</strong> ${result.qty_available}</p>
                                <p><strong>Fecha:</strong> ${result.date}</p>
                            </div>
                        `,
                        buttons: [{ text: "Cerrar", classes: "btn-primary", close: true }],
                    }).open();
                } catch (error) {
                    console.error("Error al obtener datos de stock:", error);
                }
            });
        });
    });
}

registry.category("view_hooks").add("setup_stock_info_button", setupStockInfoButton);
