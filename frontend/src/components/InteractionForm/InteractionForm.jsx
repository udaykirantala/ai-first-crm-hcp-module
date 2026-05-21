import { useSelector } from "react-redux";
import "./InteractionForm.css"
import DateIcon from '../../assets/calendar-regular.png'
import Clock from '../../assets/clock-regular.png'

export const InteractionForm = () => {

    const extractedData = useSelector(
        (state) => state.interaction.extractedData
    );
    return (
        <div className="form-container">
            <h2>Log HCP Interaction</h2>
            <p>Interaction Details</p>
            <div className="form-grid">

                <div className="hcp-name-continer label-grid">

                    <label>
                        HCP Name
                    </label>

                    <input
                        type="text"
                        readOnly
                        placeholder="Search or select HCP..."
                        value={
                            extractedData?.hcp_name || ""
                        }
                        className="input-filed"
                    />

                </div>


                <div className="Interaction-name-continer label-grid">

                    <label>
                        Interaction Type
                    </label>

                    <select
                        value={
                            extractedData?.interaction_type || ""
                        }
                        style={{
                            pointerEvents: "none"
                        }}
                        className="input-filed-dropdown"
                    >

                        <option>
                            Meeting
                        </option>

                        <option>
                            Call
                        </option>

                        <option>
                            Visit
                        </option>

                    </select>

                </div>

            </div>
            <div className="form-grid date-time">

                <div>

                    <label>
                        Date
                    </label>

                    <div className="input-icon-wrapper">

                        <input
                            type="text"
                            readOnly
                            value={
                                extractedData?.date || ""
                            }
                            className="input-filed-date-time"
                        />

                        <span className="input-icon">

                            <img
                                src={DateIcon}
                                alt="calendar-regular"
                                width='20px'
                            />

                        </span>

                    </div>

                </div>


                <div>

                    <label>
                        Time
                    </label>

                    <div className="input-icon-wrapper">

                        <input
                            type="text"
                            readOnly
                            value={
                                extractedData?.time || ""
                            }
                            className="input-filed-date-time"
                        />

                        <span className="input-icon">

                            <img
                                src={Clock}
                                alt="clock"
                                width='20px'
                            />

                        </span>

                    </div>

                </div>

            </div>
            <div className="form-grid-attendees">
                <label>
                    Attendees
                </label>
                <input
                    type="text"
                    readOnly
                    value={
                        Array.isArray(
                            extractedData?.attendees
                        )
                            ? extractedData.attendees.join(", ")
                            : extractedData?.attendees || ""
                    }
                    className="attendees-inputfiled"
                />
            </div>
            <div className="textarea-continer">
                <label className="label-topics">
                    Topics Discussed
                </label>
                <textarea
                    rows="5"
                    placeholder="Enter key discussion points..."
                    value={
                        extractedData?.topic || ""
                    }
                    readOnly
                    className="textarea-filed"
                />
            </div>
            <p className="summarize-heding">
                <span>🎙️</span>
                Summarize from Voice Note
                (Requires Consent)
            </p>
            <div className="materials-section">
                <p className="matrial-text">Materials Shared / Samples Distributed</p>
                <div className="material-box">
                    <div className="material-header">
                        <p className="matrial-text">Materials Shared</p>
                        <label className="outline-btn matrial-filed">
                            🔍 Search/Add
                            <input
                                type="file"
                                hidden
                                multiple
                                onChange={(e) => {

                                    const files =
                                        Array.from(e.target.files)
                                            .map(file => file.name);

                                    console.log(files);

                                }}
                            />
                        </label>
                    </div>
                </div>
                <div className="material-box">
                    <div className="material-header">
                        <p className="matrial-text">
                            Samples Distributed
                        </p>
                        <label className="outline-btn matrial-filed">
                            ➕ Add Sample
                            <input
                                type="file"
                                hidden
                                multiple
                                onChange={(e) => {

                                    const files =
                                        Array.from(e.target.files)
                                            .map(file => file.name);

                                    console.log(files);

                                }}
                            />
                        </label>
                    </div>
                </div>
            </div>
            <div className="sentiment-section">
                <label className="sentiment-text">
                    Observed/Inferred HCP Sentiment
                </label>
                <div className="radio-group">
                    <label>
                        <input
                            type="radio"
                            name="sentiment"
                            checked={
                                extractedData?.sentiment
                                    ?.toLowerCase() ===
                                "positive"
                            }
                            readOnly
                            className="radio-button"
                        />
                        😊 Positive
                    </label>
                    <label>
                        <input
                            type="radio"
                            name="sentiment"
                            checked={
                                extractedData?.sentiment
                                    ?.toLowerCase() ===
                                "neutral"
                            }
                            readOnly
                        />
                        😐 Neutral
                    </label>
                    <label>
                        <input
                            type="radio"
                            name="sentiment"
                            checked={
                                extractedData?.sentiment
                                    ?.toLowerCase() ===
                                "negative"
                            }
                            readOnly
                        />
                        😟 Negative
                    </label>
                </div>
            </div>
            <div className="textarea-continer">
                <label>
                    Outcomes
                </label>
                <textarea
                    rows="4"
                    readOnly
                    className="textarea-filed"
                    value={
                        Array.isArray(
                            extractedData?.outcomes
                        )
                            ? extractedData.outcomes.join(", ")
                            : extractedData?.outcomes || ""
                    }
                />
            </div>
            <div className="textarea-continer">
                <label>
                    Follow-up Actions
                </label>
                <textarea
                    rows="4"
                    className="textarea-filed"
                    value={
                        typeof extractedData?.follow_up ===
                            "object"

                            ? JSON.stringify(
                                extractedData.follow_up,
                                null,
                                2
                            )

                            : extractedData?.follow_up || ""
                    }
                    readOnly
                />
            </div>
            <button className="save-btn">
                <p className="btn-text">Save Interaction</p>
            </button>
        </div>
    );

};