pragma solidity ^0.4.0;
contract System {

    struct Device {
        bool active;
        address pos;
        string name;
        string devType;
        //Device prev;
        //Device next;
    }
    
    struct User {
        bool admin;
        bool active;
    }

    address headAdmin;
    mapping(address => User) users;
    mapping(address => Device) devices;

    /// Initialize the system, done by the headAdmin with a maestro device.
    function System(address devPos, string devType, string devName) public {
        headAdmin = msg.sender;
        users[headAdmin].admin = true;
        addBlock(devPos, devType, devName);
    }
    
    /// Create a new Block.
    function addBlock(address devPos, string devType, string devName) public {
        if (!users[msg.sender].admin || !users[msg.sender].active) return;
        devices[devPos].name = devName;
        devices[devPos].devType = devType;
        devices[devPos].active = true;
    }
    
    /// Remove a Block but keep the data.
    function removeBlock(address devPos) public {
        if (!users[msg.sender].admin || !users[msg.sender].active) return;
        devices[devPos].active = false;
    }
    
    /// Add a new user.
    function addUser(address newUser, bool isAdmin) public {
        if (!users[msg.sender].admin || !users[msg.sender].active) return;
        users[newUser].admin = isAdmin;
        users[newUser].active = true;
    }
    
    /// Remove a user.
    function removeUser(address oldUser) public {
        if (!users[msg.sender].admin || !users[msg.sender].active) return;
        users[oldUser].active = false;
    }
}