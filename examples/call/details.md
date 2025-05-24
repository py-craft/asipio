# 📞 Scenario: INVITE and BYE Call Flow

## Overview

The system handles SIP (Session Initiation Protocol) messages over UDP. Two key operations are illustrated: initiating a call with an INVITE and ending it with a BYE.

### INVITE Handling:

- When an INVITE request arrives via UDP, the system's selector detects the readable socket.

- The protocol layer reads the datagram and passes it to the application layer.

- The application schedules a dispatch task to handle the INVITE.

- This task executes the dial plan and initiates call routing logic.

- The call routing logic processes the INVITE and sends a 200 OK response to acknowledge and establish the call.

### BYE Handling:

- When a BYE request is received from the client, the flow begins similarly with the selector and protocol layers processing the datagram.

- The application dispatches the message and forwards it to the dialog handler.

- The dialog processes the BYE request, evaluates whether to close the dialog, and schedules its closure.

- A closure task is initiated, which waits for a short delay before performing cleanup.

- Finally, the dialog is removed from the application's internal state, completing the call termination process.

## Call Flow Diagram

```mermaid
sequenceDiagram
    title Call Flow Diagram (INVITE and BYE)

    participant Selector as selector_events.py:_read_ready
    participant Protocol as protocols.py:datagram_received
    participant App as application.py
    participant DispatchTask1 as Task: _dispatch (INVITE)
    participant CallRouteTask as Task: _call_route
    participant Dialog as dialog.py
    participant DispatchTask2 as Task: _dispatch (BYE)
    participant ClosureTask as Task: closure()

    %% INVITE flow
    note over Selector: Incoming UDP (INVITE)
    Selector ->> Protocol: _read_ready()
    Protocol ->> App: datagram_received()
    App ->> DispatchTask1: create_task(_dispatch)
    DispatchTask1 ->> DispatchTask1: _dispatch()
    DispatchTask1 ->> DispatchTask1: await _run_dialplan()
    DispatchTask1 ->> CallRouteTask: create_task(_call_route)
    CallRouteTask ->> CallRouteTask: _call_route()
    CallRouteTask ->> CallRouteTask: on_invite()
    CallRouteTask ->> App: send 200 OK

    %% BYE flow
    note over Selector: Client sends BYE
    Selector ->> Protocol: _read_ready()
    Protocol ->> App: datagram_received()
    App ->> DispatchTask2: create_task(_dispatch)
    DispatchTask2 ->> DispatchTask2: _dispatch()
    DispatchTask2 ->> Dialog: await dialog.receive_message()
    Dialog ->> Dialog: _receive_request()
    Dialog ->> Dialog: _maybe_close()
    Dialog ->> Dialog: close_later()
    Dialog ->> ClosureTask: create_task(closure())

    ClosureTask ->> ClosureTask: await sleep(dialog_closing_delay)
    ClosureTask ->> ClosureTask: close()
    ClosureTask ->> ClosureTask: _close()
    ClosureTask ->> App: remove dialog from _dialogs
```
