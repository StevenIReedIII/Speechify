local M = {}

function M.speechify()
    -- Save the current buffer's content to a temporary HTML file
    local buf_content = vim.api.nvim_buf_get_lines(0, 0, -1, false)
    local temp_html_path = "/tmp/current_buffer.html"
    local temp_html = io.open(temp_html_path, "w")
    for _, line in ipairs(buf_content) do
        temp_html:write(line .. "\n")
    end
    temp_html:close()

    -- Define the Python script command, passing the HTML file as an argument
    local python_cmd = "python3 /path/to/timer_app.py " .. temp_html_path

    -- Check if the Python application is running; if not, start it
    local handle = io.popen("pgrep -f 'timer_app.py'")
    local result = handle:read("*a")
    handle:close()
    if result == "" then
        vim.fn.jobstart(python_cmd)
    else
        -- If the Python app is already running, update its content
        vim.fn.system("curl -X POST --data-binary @" .. temp_html_path .. " http://localhost:5000/update")
    end
end

vim.cmd("command! Speechify lua require'speechify'.speechify()")

return M
